async function GetRequest(url) {
    response = await fetch(url)
    return await response.json()
}

async function render_products() {
    let products = await GetRequest('/products-json/');
    products_html = document.getElementsByClassName('products')[0]
    products.forEach(product => {
        html = product_template(product)
        products_html.innerHTML += html
        })
    ;
}

function product_template(product) {
    return `
    <div id="product-card-${product.id}" class="card row m-2 col-3">
        <div class="card">
            <div class="row">
                <a href="{% url 'product/${product.id}' %}">  
                    <img src="/static/images/default-product-image.png" class="card-img-top" alt="...">
                    <div class="card-body">
                    <h5 class="card-title">${product.name}</h5>
                    <p class="card-text">${product.description}</p>
                    </div>
                </a>
            </div>
            <div class="row p-3">
                <button id="product_${product.id}" onclick="append_in_order(${product.id});" class="btn btn-outline-danger">В корзину за ${product.price}Р</button>
            </div>
        </div>
    </div>
    `
}


render_products()