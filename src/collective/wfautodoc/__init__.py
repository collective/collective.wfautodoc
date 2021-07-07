from Products.DCWorkflow.DCWorkflow import DCWorkflowDefinition


DCWorkflowDefinition.manage_options += (
    {"label": "Graph (dot)", "action": "@@wfautodoc_gvfile"},
    {"label": "Graph (svg)", "action": "@@wfautodoc_svg"},
)
