import streamlit as st

# Stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

st.title("📈 Stock Portfolio Tracker")

# Session state
if "portfolio" not in st.session_state:
    st.session_state.portfolio = {}
    st.session_state.total = 0

st.subheader("Available Stocks")
for s, p in stock_prices.items():
    st.write(f"{s} : {p}")

stock = st.text_input("Enter stock name").upper()
qty = st.number_input("Enter quantity", min_value=1, step=1)

if st.button("Add Stock"):
    if stock in stock_prices:
        cost = stock_prices[stock] * qty
        st.session_state.portfolio[stock] = qty
        st.session_state.total += cost

        st.success("Stock added successfully!")
        st.write("Stock :", stock)
        st.write("Quantity :", qty)
        st.write("Cost :", cost)
        st.write("Total Investment :", st.session_state.total)
    else:
        st.error("Stock not available")

st.divider()
st.subheader("📊 Portfolio Summary")

for s, q in st.session_state.portfolio.items():
    st.write(f"{s} → {q} shares = {q * stock_prices[s]}")

st.write("### TOTAL INVESTMENT :", st.session_state.total)

# ---------- SAVE TO TXT FILE ONLY ----------
if st.button("Save Portfolio to TXT"):
    with open("portfolio.txt", "w") as f:
        f.write("STOCK PORTFOLIO SUMMARY\n")
        f.write("------------------------\n")
        for s, q in st.session_state.portfolio.items():
            f.write(f"{s} : {q} shares = {q * stock_prices[s]}\n")
        f.write("------------------------\n")
        f.write(f"TOTAL INVESTMENT = {st.session_state.total}\n")

    st.success("✅ Portfolio saved as portfolio.txt")