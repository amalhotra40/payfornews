import streamlit as st

APP_NAME = "Paying for news"


st.set_page_config(
    page_title=APP_NAME,
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title(APP_NAME)

REFERENCE = "https://policydialogue.org/publications/working-papers/paying-for-news-what-google-and-meta-owe-us-publishers-draft-working-paper/"


def add_google_search_platform(currency):
    REVENUE_DEFAULTS = 57.0e3  # in millions USD (2023)
    TIME_PERCENT_DEFAULTS = 35.0  # in percent of time spent on news
    HELP_TEXT = "Defaults for US market (2023). Modify for other markets."
    revenue_google = st.number_input(
        f"Google search ad revenue (in millions {currency})",
        value=REVENUE_DEFAULTS,
        help=HELP_TEXT,
    )
    time_percent_google = st.number_input(
        f"Fraction of user demand for news content on Google",
        value=TIME_PERCENT_DEFAULTS,
        help=f"Defaults from reference: {REFERENCE} for US market.",
        min_value=0.0,
        max_value=100.0,
    )
    split_share_google = st.slider(
        "Split share between Publisher and Google",
        0.00,
        1.00,
        0.50,
        help="Fractional split share of revenue between Publisher(left) and Google search(right), default = 0.50",
    )
    return revenue_google * time_percent_google / 100.0 * split_share_google


def add_meta_platform(currency):
    REVENUE_DEFAULTS = 28.78e3  # in millions USD (2022)
    TIME_PERCENT_DEFAULTS = 13.2  # in percent of time spent on news
    HELP_TEXT = "Defaults for US market (2022). Modify for other markets."
    revenue_meta = st.number_input(
        f"Facebook ad revenue (in millions {currency})",
        value=REVENUE_DEFAULTS,
        help=HELP_TEXT,
    )
    time_percent_meta = st.number_input(
        f"Fraction of time spent consuming news content on Facebook",
        value=TIME_PERCENT_DEFAULTS,
        help=f"Defaults from reference: {REFERENCE} for US market.",
        min_value=0.0,
        max_value=100.0,
    )
    split_share_meta = st.slider(
        "Split share between Publisher and Facebook",
        0.00,
        1.00,
        0.50,
        help="Fractional split share of revenue between Publisher(left) and Facebook(right), default = 0.50",
    )
    return revenue_meta * time_percent_meta / 100.0 * split_share_meta


with st.sidebar:
    # currency = st.selectbox("Currency", ["USD", "INR", "EUR", "Other"], index=0)
    # if currency == "Other":
    #     currency = st.text_input("Enter currency:")
    currency = "USD"
    st.subheader("Google")
    google = add_google_search_platform(currency)

    st.divider()

    st.subheader("Facebook")
    meta = add_meta_platform(currency)


total = google + meta

st.markdown(
    'A [research paper](https://policydialogue.org/publications/working-papers/paying-for-news-what-google-and-meta-owe-us-publishers-draft-working-paper/) titled _Paying for News: What Google and Meta Owe US Publishers_ by Patrick Holder, Haaris Mateen, Anya Schiffrin, and Haris Tabakovic estimates the payment that Facebook and Google Search platforms would owe to news publishers for the use of news content, if the Journalism Competition & Preservation Act (JCPA) comes into force using a novel methodology. This web-application makes it easy to calculate the "fair payment" for other markets using the methodology described in the above paper.'
)
st.markdown("#### Modify inputs in sidebar 👈 to estimate 'fair payment' ⬇️")
st.write(f"Google: ", round(google, 2), f"million {currency}.")
st.write(f"Facebook: ", round(meta, 2), f"million {currency}.")
st.write(f"Sum: ", round(total, 2), f"million {currency}.")
st.divider()

st.warning(
    """*Disclaimers:* The purpose of this application is to aid researchers to calculate numbers for their own countries and no guarantee about the accuracy of the generated "fair payment" should be assumed or expected. Furthermore, note that all data, values, methodology, and assumptions used in the underlying code come directly from the above source paper. The author of this web application is not responsible for any omissions/assumptions in the source paper. Please contact [Haaris Mateen](mailto:hmateen@uh.edu) (the lead author of the source research) for any questions or comments on the original research, including the methodology and assumptions, or if you would like to understand more about the inputs and outputs of this web application. If you find any bugs while using the application or discrepancies between the original paper and this web application, please [email here](mailto:abhinav.email.id+payingfornewswebapp@gmail.com) instead."""
)
