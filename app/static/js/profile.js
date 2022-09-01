function change_info(type, user) {
    form_html = document.getElementsByClassName(type)[0]
    new_value = form_html.value
    if (new_value !== user.type) {
        user[type] = new_value
    }
    console.log('5')
}