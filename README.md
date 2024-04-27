# aalto-ai-hackathon
Install virtual environment by running
```bash
python -m venv python-env
```

Activate it by
```bash
source python-env/bin/activate
```

Use pip to install the required packages
```bash
pip install openai pypdf2 python-docx
```

This script is used the following way:
```bash
python main.py FILENAME
```

The analysis will be exported to FILENAME-analysis-(date).json

Remember to include your OpenAI API key in api-key.txt (echo your key there)

Also included with this repo is a little handle.py file which will check a json file and delete it and the file if there is no product to be bought.
