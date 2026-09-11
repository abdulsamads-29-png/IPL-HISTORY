# IPL Streamlit Data Analysis Dashboard

This project is based on the uploaded practical lab guide for the IPL Data Analysis and Visualization multi-page Streamlit application.

## Project structure

```text
IPL_Streamlit_Project/
├── app.py
├── IPL_2008_2026_Merged.csv
├── requirements.txt
└── pages/
    ├── 1_About_Project.py
    ├── 2_Data_Analysis.py
    └── 3_Data_Visualization.py
```

The PDF specifies the IPL CSV dataset as `IPL_2008_2026_Merged.csv`. The uploaded PDF did not include the CSV itself, so place that CSV in the project root.

## Install

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

## Demo login

Username: `admin`
Password: `1234`

These credentials are only for the classroom/demo login described in the lab guide, not production authentication.
