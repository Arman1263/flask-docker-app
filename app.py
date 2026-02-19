from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Docker App</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, Helvetica, sans-serif;
        }

        body {
            height: 100vh;
            background: linear-gradient(135deg, #0f172a, #1e293b);
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
        }

        .container {
            width: 100%;
            max-width: 500px;
            padding: 20px;
        }

        .card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            padding: 40px;
            border-radius: 16px;
            text-align: center;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
        }

        h1 {
            margin-bottom: 10px;
        }

        p {
            margin-bottom: 20px;
            color: #cbd5e1;
        }

        button {
            padding: 12px 24px;
            border: none;
            border-radius: 8px;
            background: #38bdf8;
            color: black;
            font-weight: bold;
            cursor: pointer;
            transition: 0.2s ease;
        }

        button:hover {
            background: #0ea5e9;
        }

        #status {
            margin-top: 20px;
            font-weight: bold;
            color: #22c55e;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="card">
        <h1>Arman + Docker</h1>
        <p>I am Arman and I believe to build stuffs.</p>

        <button onclick="checkHealth()">Check Health</button>
        <p id="status"></p>
    </div>
</div>

<script>
async function checkHealth() {
    const res = await fetch("/health");
    const data = await res.json();
    document.getElementById("status").innerText =
        "Health Status: " + data.status;
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

@app.route("/health")
def health():
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) ## 0.0.0.0 becoz to run on all devices -- out of docker container