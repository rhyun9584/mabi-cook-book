// 방법 전체 버튼
$("#method-all").change(function (){
    const beChecked = $("#method-all").prop("checked");
    $(".method-filter").prop("checked", beChecked);
})
// 방법 개별 버튼
for (const filter of document.querySelectorAll(".method-filter")){
    filter.addEventListener("change", function (){
        if (filter.checked){
            const checked_list = $(".method-filter:checked");
            if (checked_list.length === 16){
                $("#method-all").prop("checked", true);
            }
        }
        else{
            $("#method-all").prop("checked", false);
        }
    })
}

// 수집여부 전체 버튼
$("#collected-all").change(function (){
    const beChecked = $("#collected-all").prop("checked");
    $(".collected-filter").prop("checked", beChecked);
})
// 수집여부 개별 버튼
for (const collected of document.querySelectorAll(".collected-filter")){
    collected.addEventListener("change", function (){
        if (collected.checked){
            const checked_list = $(".collected-filter:checked");
            if (checked_list.length === 3){
                $("#collected-all").prop("checked", true);
            }
        }
        else{
            $("#collected-all").prop("checked", false);
        }
    })
}

// 필터 적용 버튼
const filter_btn = document.querySelector(".modal-footer button");
filter_btn.addEventListener("click", function (){
    // 방법이 전부 체크되어있지 않은 경우 조건 체크 필요
    let method_query = "";
    let collected_query = "";

    if($("#method-all").prop("checked") === false){
        const checked_list = document.querySelectorAll(".method-filter:checked");

        for (method of checked_list){
            method_query += method.id + " ";
        }
    }
    if($("#collected-all").prop("checked") === false){
        const checked_list = document.querySelectorAll(".collected-filter:checked");
        for (collected of checked_list){
            collected_query += collected.id.substr(-1) + " ";
        }
    }

    // 검색조건 유지
    const range = $("#r option:selected").val();
    const query = $("input[name=q]").val();

    const current_origin_url = window.location.origin;
    location.href = current_origin_url+`/book/?r=${range}&q=${query}&m=${method_query}&c=${collected_query}`;
})


// method, collected 필터 적용 상태 반영
window.addEventListener("pageshow", function (){
    const method_all = document.querySelector("#method-all");
    const collected_all = document.querySelector("#collected-all");

    const params = new URLSearchParams(window.location.search);

    // method 필터 상태 반영
    const method = params.get('m');
    if (method !== null && method !== ''){
        const param_list = method.split(" ");
        param_list.pop();

        const method_list = document.querySelectorAll(".method-filter");
        const unchecked_list = Array.from(method_list).filter(x => !param_list.includes(x.id));

        for (unchecked of unchecked_list){
            unchecked.checked = false;
        }
        method_all.checked = false;
    }
    else if (!method_all.checked){
        method_all.checked = true;

        const e = new Event('change');
        method_all.dispatchEvent(e);
    }

    // collected 필터 상태 반영
    const collected = params.get('c');
    if (collected !== null && collected !== ''){
        const param_list = collected.split(" ");

        const collected_list = document.querySelectorAll(".collected-filter");
        const unchecked_list = Array.from(collected_list).filter(x => !param_list.includes(x.id.substr(-1)));

        for (unchecked of unchecked_list){
            unchecked.checked = false;
        }
        collected_all.checked = false;
    }
    else if (!collected_all.checked){
        collected_all.checked = true;

        const e = new Event('change');
        collected_all.dispatchEvent(e);
    }

    // 필터 적용시 필터 버튼 표시 변경
    if(method_all.checked === false || collected_all.checked === false){
        const filter_btn = document.querySelector("#filter-btn");
        filter_btn.classList.replace("btn-outline-info", "btn-info");
    }
})