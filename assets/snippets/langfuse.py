from langfuse import Langfuse

lf = Langfuse()  # Clés issues de l'env

# 1. Toutes les étapes de l'agent sont déjà des traces requêtables.
#    Il n'a pas été nécessaire d'ajouter des events/attributes.
#    Les KPI viennent de l'observability qui était déjà capturée.
page = await lf.async_api.trace.list(
    from_timestamp=start, to_timestamp=end,
    fields="core,io,metadata",        # seulement fetch le nécessaire
    order_by="timestamp.desc",
)
traces = page.data
total_pages = page.meta.total_pages   # permet de fetch en parallèle 

# 2. Les traces ont un `session_id`, les métriques sont faciles à grouper. 
by_session: dict[str, list] = defaultdict(list)
for t in traces:
    by_session[t.session_id].append(t)

# 3. Les observations sont typées (TOOL, GENERATION, etc) avec I/O structurée,
#    ce qui permet de reconstruire ce que l'agent a fait a posteriori:
#    quelle stratégie utilisée, savoir si le RAG a retourné des documents, ...
for obs in observations:                     # from GET /api/public/v2/observations
    if obs["type"] == "TOOL" and obs["name"] == "strategy_management":
        kpi["strategy_selected"] = True
    if RAG_EMPTY_SENTINEL in str(obs["output"]):
        kpi["rag_empty"] = True
