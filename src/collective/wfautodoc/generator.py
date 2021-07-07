from functools import reduce


def wrap(text, width):
    """
    A word-wrap function that preserves existing line breaks
    and most spaces in the text. Expects that existing line
    breaks are posix newlines (\n).
    """
    wrapped = reduce(
        lambda line, word, width=width: "%s%s%s"
        % (
            line,
            " \n"[
                (
                    len(line) - line.rfind("\n") - 1 + len(word.split("\n", 1)[0])
                    >= width
                )
            ],
            word,
        ),
        text.split(" "),
    )
    return wrapped.replace("\n", "<BR />")


def generate_gv(context):
    dot = "digraph %s  {\n" % context.getId()
    wf = context
    state_to_trans = []
    for state in wf.states.values():
        roles = state.getAvailableRoles()
        roles.sort()
        permtable = [
            [
                '<FONT POINT-SIZE="10">%s</FONT>' % _
                for _ in ["permission", "acquired"] + [wrap(_, 15) for _ in roles]
            ]
        ]
        for perm in state.getManagedPermissions():
            pinfo = state.getPermissionInfo(perm)
            row = [wrap(perm, 15), pinfo["acquired"] and "X" or "."]
            row += [_ in pinfo["roles"] and "X" or "." for _ in roles]
            permtable.append(row)
        table = f'<TABLE BORDER="0"><TR><TD colspan="{len(roles)+2}" bgcolor="lightgrey"><B>{state.title or state.getId()}</B></TD></TR>\n'
        cnt = 1
        for row in permtable:
            cnt += 1
            table += "<TR>"
            bgcolor = cnt % 2 and ' BGCOLOR="lightyellow"' or ""
            for cell in row:
                table += '<TD%s><FONT POINT-SIZE="10">%s</FONT></TD>' % (bgcolor, cell)
            table += "</TR>\n"
        table += "</TABLE>"
        dot += f'"{state.getId()}" [label=<{table}> shape=Mrecord];'
        dot += "\n"
        for trans in state.transitions:
            state_to_trans.append((state.getId(), trans))

    for state, trans in state_to_trans:
        tob = wf.transitions[trans]
        table = '<TABLE BORDER="0" BGCOLOR="lightgrey"><TR><TD colspan="2">'
        table += wrap(tob.title or tob.getId(), 19)
        table += '<BR /><FONT POINT-SIZE="10">id=%s</FONT>' % trans
        proptable = []
        table += "</TD></TR>\n"
        guard = tob.getGuard()
        if guard.permissions:
            proptable.append(["permissions", "<BR />".join(guard.permissions)])
        if guard.roles:
            proptable.append(["roles", "<BR />".join(guard.roles)])
        if guard.groups:
            proptable.append(["groups", "<BR />".join(guard.groups)])
        if guard.getExprText():
            proptable.append(["expression", guard.getExprText()])
        cnt = 0
        for key, value in proptable:
            bgcolor = cnt % 2 and ' BGCOLOR="lightyellow"' or ""
            table += "<TR>"
            table += '<TD%s><FONT POINT-SIZE="10">%s:</FONT></TD>' % (bgcolor, key)
            table += '<TD%s ALIGN="LEFT"><FONT POINT-SIZE="10">%s</FONT></TD>' % (
                bgcolor,
                value,
            )
            table += "</TR>\n"
        table += "</TABLE>"
        dot += '"%s" -> "%s" [label=<%s>, arrowhead=normal];\n' % (
            state,
            tob.new_state_id,
            table,
        )
    dot += "}\n"
    return dot
