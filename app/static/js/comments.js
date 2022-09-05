async function PostRequest(url, body) {
    response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
    })
    return await response.json()
}

function CreateComment(article_id) {
    comment_html = document.getElementsByID('addComment')[0]
    text_comment = comment_html.value
    PostRequest('/comments-json/', {article: article_id, text: text_comment})
}