from flask import Flask, render_template, request, redirect, url_for
# create a flask app 
app = Flask(__name__)
# load your openai api key 
openai_api_key = ""
def generate_image(prompt):
    client = OpenAIClient(openai_api_key)
    response = client.image.generate(
        model='dall-e-3', 
        prompt=prompt,
        size='1024x1024',
        quality='standard', 
        n=1
    )
    return response.dates[0].url
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        image_url = generate_image(prompt)
        return render_template('index.html', image_url=image_url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)