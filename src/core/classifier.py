class Result:
    def __init__(self, agent, entities):
        self.agent = agent
        self.entities = entities


def classify(query, llm=None):
    q = query.lower()

    # --- customer support ---
    if any(w in q for w in ["login", "account", "bank", "transaction", "didn't go through"]):
        agent = "customer_support"

    # --- financial planning ---
    elif any(w in q for w in ["retire", "retirement", "college", "house", "fire plan", "save"]):
        agent = "financial_planning"

    # --- financial calculator ---
    elif any(w in q for w in ["invest", "monthly", "%", "convert", "future value", "tax"]):
        agent = "financial_calculator"

    # --- predictive analysis ---
    elif any(w in q for w in ["predict", "where will"]):
        agent = "predictive_analysis"

    # --- product recommendation ---
    elif any(w in q for w in ["recommend", "which fund", "best"]):
        agent = "product_recommendation"

    # --- risk assessment ---
    elif any(w in q for w in ["risk", "drawdown", "beta", "stress", "downside", "exposed"]):
        agent = "risk_assessment"

    # --- investment strategy ---
    elif any(w in q for w in ["should i", "buy", "sell", "rebalance", "good time", "split"]):
        agent = "investment_strategy"

    # --- portfolio health ---
    elif any(w in q for w in ["portfolio", "diversified", "holdings", "concentration", "health"]):
        agent = "portfolio_health"

    # --- market research ---
    elif any(w in q for w in [
        "price", "news", "compare", "rate", "gainers",
        "markets", "market", "doing", "happening",
        "aapl", "asml", "nvidia", "tesla", "nikkei", "gold", "ftse"
    ]):
        agent = "market_research"

    # --- general query ---
    else:
        agent = "general_query"

    # --- entity extraction ---
    entities = {}

    known_tickers = {
        "AAPL", "NVDA", "MSFT", "TSLA", "GOOGL", "GOOG",
        "AMZN", "META", "ASML", "HSBC", "BARC"
    }

    company_to_ticker = {
        "apple": "AAPL",
        "nvidia": "NVDA",
        "tesla": "TSLA",
        "microsoft": "MSFT",
        "google": "GOOGL",
        "amazon": "AMZN",
        "meta": "META",
        "barclays": "BARC"
    }

    clean_query = (
        query.replace("?", "")
        .replace(",", "")
        .replace(".", " ")
        .replace("!", "")
    )

    tokens = clean_query.split()
    tickers = []

    for token in tokens:
        token_upper = token.upper()

        if token_upper in known_tickers:
            tickers.append(token_upper)

        token_lower = token.lower()
        if token_lower in company_to_ticker:
            tickers.append(company_to_ticker[token_lower])

    if tickers:
        entities["tickers"] = list(dict.fromkeys(tickers))

    return Result(agent, entities)