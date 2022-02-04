$(document).ready(function(){
    const userInputId = getCookie("userInputId");
    $("input[name='email']").val(userInputId);

    // 쿠키에서 가져온 값이 있는 경우
    if($("input[name='email']").val() !== ""){
        $("#saveId").attr("checked", true);
    }

    // 체크 박스에 변화가 있는 경우
    $("#saveId").change(function (){
        // ID 저장하기 체크한 경우
        if($("#saveId").is(":checked")){
            const userInputId = $("input[name='email']").val();
            setCookie("userInputId", userInputId, 7); // 7일 동안 쿠키 저장
        } else {
            // ID 저장하기 체크 해제
            deleteCookie("userInputId");
        }
    });

    // ID 저장하기를 체크한 상태로 ID를 입력하는 경우, ID 저장 값 추가 갱신
    $("input[name='email']").keyup(function (){
        if($("#saveId").is(":checked")){
            const userInputId = $("input[name='email']").val();
            setCookie("userInputId", userInputId, 7);
        }
    });
});


function setCookie(cookieName, value, expireDays){
    const today = new Date();
    today.setDate(today.getDate() + expireDays);

    // cookie 저장 시 "key=value; expires=(GMT 형식)"의 형식으로 저장
    const cookieValue = escape(value) + ((expireDays == null) ? "" : "; expires=" + today.toGMTString());
    document.cookie = cookieName + "=" + cookieValue;
}

function deleteCookie(cookieName){
    const expireDate = new Date();
    expireDate.setDate(expireDate.getDate() - 1);
    document.cookie = cookieName + "= " + "; expires=" + expireDate.toGMTString();
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