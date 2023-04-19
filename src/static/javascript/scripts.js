function updateChatGPTButton() {
    checkedBoxes = document.querySelectorAll('.recipe-checkbox:checked')
    document.getElementById('chat-gpt-button').disabled = checkedBoxes.length !== 2
}

function registerCheckboxListener() {
    recipeCheckboxes = document.querySelectorAll('.recipe-checkbox')
    recipeCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('click', updateChatGPTButton)
    })
}

window.onload = () => {
    document.getElementById('recipe_form').addEventListener('submit', async event => {
        event.preventDefault()
        const response = await fetch('/generate_recipes', { method: 'POST', body: new FormData(event.target) })
        const resultHtml = await response.text()
        document.getElementById('results').innerHTML = resultHtml
        registerCheckboxListener()
    })

    document.getElementById('chat-gpt-button').addEventListener('click', event => {
        event.target.classList.add('loading')
        window.setTimeout(() => {
            const modal = new bootstrap.Modal(document.getElementById('chatGPTModal'))
            modal.show()
            event.target.classList.remove('loading')
        }, 1000)
    })
}