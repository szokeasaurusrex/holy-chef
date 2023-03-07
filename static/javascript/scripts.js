window.onload = () => {
    document.getElementById('recipe_form').addEventListener('submit', async event => {
        event.preventDefault()
        const response = await fetch('/generate_recipes', { method: 'POST', body: new FormData(event.target) })
        const resultHtml = await response.text()
        document.getElementById('results').innerHTML = resultHtml
    });
}