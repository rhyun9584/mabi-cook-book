const cook_list = document.querySelectorAll(`#cook .cook-content`);

for (i = 0; i < cook_list.length; i++){
    const cook = cook_list[i];

    const btn = cook.querySelector("#collect-btn");
    btn.addEventListener("click", function(){
        const state = parseInt(cook.className.substr(-1));
        const new_state = (state + 1) % 3;

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
                } else {
                    alert("서버와의 통신 에러가 발생하여 변경사항을 반영하지 못하였습니다.")
                }
            })
            .catch(err => console.error(err))
    });
}
