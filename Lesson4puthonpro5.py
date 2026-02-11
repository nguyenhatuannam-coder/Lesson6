import streamlit as st
import pandas as pd


df = pd.read_csv("most-popular_updated_15_feb.csv")

st.subheader("Bảng dữ liệu Top 20")
st.dataframe(df.head(20))


chart = {
    "mark": "bar",
    "encoding": {
        "x": {
            "field": "show_title",
            "type": "nominal",
            "title": "Tên phim",
            "sort": "-y",
            "axis": {"labelAngle": -45}
        },
        "y": {
            "field": "hours_viewed_first_28_days",
            "type": "quantitative",
            "title": "Giờ xem trong 28 ngày đầu"
        },
        "tooltip": [
            {"field": "show_title", "type": "nominal", "title": "Phim"},
            {
                "field": "hours_viewed_first_28_days",
                "type": "quantitative",
                "title": "Giờ xem"
            }
        ]
    }
}

st.subheader("Biểu đồ cột: Giờ xem trong 28 ngày đầu")
st.vega_lite_chart(df.head(20), chart, use_container_width=True)
