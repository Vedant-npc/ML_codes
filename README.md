# ML Practical Code Finder

A Streamlit app that displays a practical's Python code from a URL query parameter.

## Run locally

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

Try:
- `http://localhost:8501/?practical=1`
- `http://localhost:8501/?practical=2`

## Add your practicals

Edit `practicals.py` and add entries to `PRACTICALS`. Use a unique integer as the key.

## Deploy publicly

1. Push these files to a GitHub repository.
2. Open Streamlit Community Cloud: https://share.streamlit.io/
3. Create a new app and select your repository.
4. Set the main file path to `app.py`.
5. Deploy. Streamlit will provide your public app URL.

Then share links like:
`https://YOUR-APP-NAME.streamlit.app/?practical=1`
