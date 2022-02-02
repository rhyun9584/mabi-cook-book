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
    location.href = `http://127.0.0.1:5000/book/?r=${range}&q=${query}&m=${method_query}&c=${collected_query}`;
})

// function getCookie(cookieName){
//     cookieName = cookieName + '=';
//     const cookieData = document.cookie;
//     let start = cookieData.indexOf(cookieName);
//
//     let cookieValue = '';
//     if(start !== -1){
//         start += cookieName.length;
//         let end = cookieData.indexOf(';', start);
//
//         if (end === -1) end = cookieData.length;
//         cookieValue = cookieData.substring(start, end);
//     }
//     return unescape(cookieValue);
// }
//
// $(document).ready(function (){
//     // 캐싱된 method, collected 필터 적용 상태 반영
//     const all_method = document.querySelector("#method-all");
//     const all_collected = document.querySelector("#collected-all");
//
//     const method = getCookie('method');
//     if (method !== ''){
//         let method_list = method.split(" ");
//         console.log(method_list)
//         method_list.pop();
//         console.log(method_list)
//
//         const method_check_list = document.querySelectorAll(".method-filter");
//         const unchecked_list = Array.from(method_check_list).filter(x => !method_list.includes(x.id));
//
//         for (unchecked of unchecked_list){
//             unchecked.checked = false;
//         }
//
//         all_method.checked = false;
//     }
//
//     const collected = getCookie('collected');
//     if (collected !== ''){
//         let collected_list = collected.split(" ");
//         collected_list.pop();
//     }
//
//     if(all_method.checked === false || all_collected.checked === false){
//         const filter_btn = document.querySelector("#filter-btn");
//         filter_btn.classList.replace("btn-outline-info", "btn-info");
//     }
// })