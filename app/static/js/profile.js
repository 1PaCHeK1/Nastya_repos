async function render_profile() {
    users = await GetRequest('/users-json/');
    profile_html = document.getElementsByID('new_value')
    users.forEach(product => {
        html = product_template(product)
        products_html.innerHTML += html
        })
    ;
}


async function GetRequest(url) {
    response = await fetch(url)
    return await response.json()
}

async function change_info(type, user_id) {
    let users = await GetRequest('/users-json/');
    for (let i = 0; i < users.length; index++) {
        if (users[i]['id'] == user_id) {
            user = users[i]
            break
        }
    form_html = document.getElementsByClassName(type)[0]
    new_value = form_html.value
    if (new_value !== user[type]) {
        user[type] = new_value
    }
    console.log('5')
        
    }
}
