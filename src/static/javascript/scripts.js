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

    document.getElementById('chat-gpt-button').addEventListener('click', async event => {
        event.target.classList.add('loading')
        const response = await fetch('/chat_gpt_combine', { method: 'POST' })
        const resultHTML = await response.text()
        document.getElementById('chatGPTModal').innerHTML = resultHTML
        const modal = new bootstrap.Modal(document.getElementById('chatGPTModal'))
        modal.show()
        event.target.classList.remove('loading')
    })
}