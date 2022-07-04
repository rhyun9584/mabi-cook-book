jQuery.validator.setDefaults({
    errorElement: "div",
    errorPlacement: function (error, element) {
        error.addClass('invalid-feedback');
        console.log(element.closest('.form-group'))
        element.closest('div').append(error);
    },
})

$("#signup-form").validate({
    rules: {
        email: {
            required: true,
            email: true,
        },
        password1: {
            required: true,
            minlength: 6,
        },
        password2: {
            required: true,
            equalTo: '#password1',
        },
        server: {
            required: true,
        },
        name: {
            required: true,
        },
    },
    messages: {
        email: {
            required: "* 이메일 ID를 입력해주세요.",
            email: "* 이메일 형식으로 입력해주세요."
        },
        password1: {
            required: "* 비밀번호를 입력해주세요.",
            minlength: "* 6자 이상 입력해주세요.",
        },
        password2: {
            required: "* 비밀번호 확인을 입력해주세요.",
            equalTo: "* 비밀번호가 일치하지 않습니다.",
        },
        server: {
            required: "* 서버를 선택해주세요.",
        },
        name: {
            required: "* 닉네임을 입력해주세요.",
        },
    },
});

$("#signin-form").validate({
    rules: {
        email: {
            required: true,
        },
        password: {
            required: true,
        },
    },
    messages: {
        email: {
            required: "* 이메일 ID를 입력해주세요.",
        },
        password: {
            required: "* 비밀번호를 입력해주세요.",
        }
    },
});

$("#changepw-form").validate({
    rules: {
        old_pw: {
            required: true,
        },
        new_pw1: {
            required: true,
            minlength: 6,
        },
        new_pw2: {
            required: true,
            equalTo: "#new_pw1",
        },
    },
    messages: {
        old_pw: {
            required: "* 현재 비밀번호를 입력해주세요.",
        },
        new_pw1: {
            required: "* 새 비밀번호를 입력해주세요.",
            minlength: "* 6자 이상 입력해주세요.",
        },
        new_pw2: {
            required: "* 새 비밀번호 확인을 입력해주세요.",
            equalTo: "* 새 비밀번호가 일치하지 않습니다.",
        },
    },
});

$("#searchpw-form").validate({
    rules: {
        email: {
            required: true,
        },
    },
    messages: {
        email: {
            required: "* 이메일 ID를 입력하세요.",
        },
    },
});

$("#resetpw-form").validate({
    rules: {
        new_pw1: {
            required: true,
            minlength: 6,
        },
        new_pw2: {
            required: true,
            equalTo: "#new_pw1",
        },
    },
    messages: {
        new_pw1: {
            required: "* 새 비밀번호를 입력해주세요.",
            minlength: "* 6자 이상 입력해주세요.",
        },
        new_pw2: {
            required: "* 새 비밀번호 확인을 입력해주세요.",
            equalTo: "* 새 비밀번호가 일치하지 않습니다.",
        },
    }
});

$("#leave-form").validate({
    rules: {
        password: { required: true },
    },
    messages: {
        password: { required: "* 비밀번호를 입력해주세요." },
    },
});
