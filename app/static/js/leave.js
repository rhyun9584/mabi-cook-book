const leaveForm = document.getElementById("leave-form");

leaveForm.addEventListener('submit', function (event){
    const result = confirm("정말 탈퇴하시겠습니까?");

    if (result === true){
        this.submit();
    } else {
        return false;
    }
})