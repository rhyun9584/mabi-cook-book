const search_form = document.querySelector("#search-form");

search_form.addEventListener("submit", function (){
    const params = new URLSearchParams(window.location.search);

    const method = params.get('m');
    const collected = params.get('c');

    if (method !== null){
        const method_element = createHiddenInput("m", method);
        search_form.append(method_element);
    }
    if (collected !== null){
        const collected_element = createHiddenInput("c", collected);
        search_form.append(collected_element);
    }
})

function createHiddenInput(name, value){
    const element = document.createElement("input");
    element.type = "hidden";
    element.name = name;
    element.value = value;

    return element;
}

// range 선택
window.addEventListener("pageshow", function (){
    const params = new URLSearchParams(window.location.search);

    let range = params.get('r');
    if(range === null){ range = 'all'; }

    $('#r').val(range).prop("selected", true);
})
