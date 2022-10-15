const cook_list = document.querySelectorAll(`#cook .cook-content`);

const STATE_CHANGE_API = '/book/change_state/';

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
            "cook_id": parseInt(cook.id.substr(4)),
            "new_state": new_state,
        }

        const current_origin_url = window.location.origin;
        fetch(current_origin_url+STATE_CHANGE_API, {
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
