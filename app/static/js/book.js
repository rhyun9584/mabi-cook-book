const cook_list = document.querySelectorAll(`#cook .cook-content`);

for (i = 0; i < cook_list.length; i++){
    const cook = cook_list[i];

    const btn = cook.querySelector("#collect-btn");

    const state = parseInt(cook.className.substr(-1));
    const icon = getStateIcon(state);
    btn.removeChild(btn.firstChild);
    btn.append(icon);

    btn.addEventListener("click", function(){
        const state = parseInt(cook.className.substr(-1));
        const new_state = (state + 1) % 3;

        const new_icon = getStateIcon(new_state);

        // db 정보 업데이트
        const json = {
            "cook_id": parseInt(cook.id.substr(-1)),
            "new_state": new_state,
        }

        fetch('http://127.0.0.1:5000/book/change_state/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(json)
        })
            .then(res => {
                if (res.status === 200){
                    cook.classList.replace(`bg-collect${state}`, `bg-collect${new_state}`);
                    btn.removeChild(btn.firstChild);
                    btn.append(new_icon);
                } else {
                    alert("서버와의 통신 에러가 발생하여 변경사항을 반영하지 못하였습니다.")
                }
            })
            .catch(err => console.error(err))
    });
}

function getStateIcon(state){
    const icon = document.createElement('i');
    icon.classList.add('bi');

    let icon_name = 'bi-star';
    switch (state){
        case 1:
            icon_name += '-half';
            break;
        case 2:
            icon_name += '-fill';
            break;
    }
    icon.classList.add(icon_name);

    return icon
}

function getCookie(cookieName){
    cookieName = cookieName + '=';
    const cookieData = document.cookie;
    let start = cookieData.indexOf(cookieName);

    let cookieValue = '';
    if(start !== -1){
        start += cookieName.length;
        let end = cookieData.indexOf(';', start);

        if (end === -1) end = cookieData.length;
        cookieValue = cookieData.substring(start, end);
    }
    return unescape(cookieValue);
}

// range 선택
$(document).ready(function(){
    const range = getCookie('range');
    $('#r').val(range).prop("selected", true);
});