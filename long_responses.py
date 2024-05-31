import random
 
R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_SUGGESTION ="Invest 20% of your savings into large cap, mid cap, small cap in a 50:30:20 ratio"
R_GENSUGGESTION ="Life insurance is suggested after the age of 30 along with health insurance."
R_LARGECAP = "Large-cap (sometimes called big cap) refers to a company with a market capitalization value of more than $10 billion."
R_MIDCAP ="Mid-cap stocks are shares of companies with total market capitalization in the range of about $2 billion to $10 billion. Along with large-cap stocks and small-cap stocks, mid-cap stocks are one of the three main stock categories and offer a compromise between the growth, risk and volatility tradeoffs of their larger and smaller counterparts."
R_SMALLCAP ="A small-cap stock is generally that of a company with a market capitalization of between $300 million and $2 billion."
 
 
def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response