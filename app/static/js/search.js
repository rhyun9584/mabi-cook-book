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

window.addEventListener("pageshow", function (){
    const params = new URLSearchParams(window.location.search);

    // range 선택
    let range = params.get('r');
    if(range === null){ range = 'all'; }

    $('#r').val(range).prop("selected", true);

    // 검색어 하이라이팅
    const search = params.get('q');

    let class_range = ''
    if (range === 'all') { class_range='.cook-kor-name, .cook-ingredients' }
    else if (range === 'name'){ class_range = '.cook-kor-name' }
    else if (range === 'ingredients'){ class_range = '.cook-ingredients'}

    $(`${class_range}:contains('${search}')`).each(function () {
        var regex = new RegExp(search,'g');
        $(this).html( $(this).text().replace(regex, `<span class='txt-hlight'>${search}</span>`) );
    });
})
