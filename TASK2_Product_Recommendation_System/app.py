import streamlit as st
from recommendation import recommend_products

st.set_page_config(
    page_title="Product Recommendation System",
    page_icon="🛍️",
    layout="wide"
)

st.title("🛍️ Product Recommendation System")
st.write("Discover similar electronic products with AI-powered recommendations and localized pricing.")

search = st.text_input(
    "🔍 Search Product",
    placeholder="Example: phone case"
)

products = recommend_products(search)

col1, col2, col3 = st.columns(3)

col1.metric("Products", len(products))
usd_to_inr = 96.35

col2.metric(
    "Average Price",
    f"₹{products['price'].mean() * usd_to_inr:.2f}"
)

col3.metric(
    "Highest Price",
    f"₹{products['price'].max() * usd_to_inr:.2f}"
)

st.divider()

for _, row in products.iterrows():

    price = row["price"]

    discount = row["discount"] if row["discount"] else "No Discount"

    rank = row["rank-title"] if row["rank-title"] else "Not Available"

    category = row["rank-sub"] if row["rank-sub"] else "Not Available"

    colors = row["color-count"] if str(row["color-count"]) != "nan" else "N/A"

    st.container(border=True)

    st.markdown(f"### {row['goods-title-link--jump']}")

    st.write(f"💰 Price: ₹{price * usd_to_inr:.2f}")

    st.write(f"🏷️ **Discount:** {discount}")

    st.write(f"⭐ **Rank:** {rank}")

    st.write(f"📂 **Category:** {category}")

    st.write(f"🎨 **Colors:** {colors}")

    st.markdown(
        f"[🔗 View Product]({row['goods-title-link--jump href']})"
    )

    st.divider()

csv = products.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Results",
    csv,
    "recommended_products.csv",
    "text/csv"
)

st.markdown("---")
st.markdown(
    "<center><b>Developed by Srija</b></center>",
    unsafe_allow_html=True
)