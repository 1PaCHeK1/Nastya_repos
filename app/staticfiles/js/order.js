async function GetRequest(url) {
    response = await fetch(url)
    return await response.json()
}

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

function downolad_order() {
    order = localStorage.getItem('order')
    if (order === null){ order = [] }
    else { order = JSON.parse(order) }

    return order
}

function change_button(product_id) {
    btn = document.getElementById('product_' + product_id)
    if(btn!==null)
    {
        btn.onclick = () => window.open('/order/');
        btn.textContent = "Перейти в корзину";
    }
}

function init_order() {
    let order = downolad_order();
    for (const index in order) {
        change_button(order[index].product_id);
    }
}

function append_in_order(product_id) {    
    let order = downolad_order();
    
    let containt = false;

    for (const index in order) {
        if(product_id == order[index].product_id){
            order[index].amount += 1
            containt = true;
            element = document.getElementById('product_'+ product_id + '_amount')
            if (element != null) {
                element.value = order[index].amount 
            }
            
            break
        }
    }
    
    if(!containt) {
        order.push({
            product_id: product_id,
            amount: 1
        })
    } 
    console.log(order)
    localStorage.setItem('order', JSON.stringify(order))
    change_button(product_id)
}

function pop_in_order(product_id) {
    for (const index in order) {
        if(product_id == order[index].product_id){
            if(order[index].amount == 1){
                order.pop(index)
                element = document.getElementById('product-card-' + product_id)
                element.remove()
            }
            else {
                order[index].amount -= 1
                element = document.getElementById('product_'+ product_id + '_amount')
                element.value = order[index].amount
                
            }
            break
        }
    }
    localStorage.setItem('order', JSON.stringify(order))
    console.log(order)
}

async function render_order() {
    let orders = await GetRequest('/order-json/');
    orders_html = document.getElementsByClassName('orders')[0]
    orders.forEach(order => {
        orders_html.innerHTML += `<div class="order-${order.id} row m-2"><h1>Заказ № ${order.id}</h1></div>`
        order_html = document.getElementsByClassName(`order-${order.id}`)[0]
        order.products.forEach(product => {
            html = template_product(product)
            order_html.innerHTML += html
        })
    });
}

function template_product(product) {
    try {
        product_amount = downolad_order().filter(elem => elem.product_id === product.id)[0].amount    
    } catch (error) {
        product_amount = 1
    }
    return `
    <div id="product-card-${product.id}" class="col-3 p-1">
        <div class="card">
            <div class="row">
                <a href='/product/{{ product.id }}'>  
                    <img src="/static/images/default-product-image.png" class="card-img-top" alt="...">
                    <div class="card-body">
                    <h5 class="card-title">${product.name}</h5>
                    <p class="card-text">${product.price}Р</p>
                    </div>
                </a>
            </div>

            <div class='count_box m-3'>
                <div id="product_pop_${product.id}" onclick="pop_in_order(${product.id});" class="minus">-</div>
                <input id="product_${product.id}_amount" class='inp_price' type="text" value="${product_amount}"/>
                <div id="product_add_${product.id}" onclick="append_in_order(${product.id});" class="plus">+</div>
            </div>
        </div>
    </div>
    `
}
{/* <div class="row p-3">
    <button id="product_add_${product.id}" onclick="append_in_order(${product.id});" class="btn btn-outline-danger">${product_amount}+1</button>
    <button id="product_pop_${product.id}" onclick="pop_in_order(${product.id});" class="btn btn-outline-danger">${product_amount}-1</button>
</div> */}

function sendOrder() {
    let order = downolad_order().map(e => e.product_id);

    PostRequest('/order-json/', {products: order})
}

init_order()
render_order()