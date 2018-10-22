function validateForm(){
            var usernameEle=document.getElementById('input1') ;
            var usernameEleVal=entities(usernameEle.value);
            var passwordEle=document.getElementById('input2');
            var passwordEleVal=entities(passwordEle.value);
            var passwordEle2=document.getElementById('input3');
            var passwordEleVal2=entities(passwordEle2.value);
            if (usernameEleVal.length == 0){
                window.alert('用户名为必填项!');
                usernameEle.focus();
                return false;}
            if (usernameEleVal.length < 6){
                window.alert('用户名不能小于6位!');
                usernameEle.focus();
                return false;}
            if (passwordEleVal.length == 0){
                window.alert('密码为必填项!');
                passwordEle.focus();
                return false;}
            if (passwordEleVal.length < 8){
                window.alert('密码不能小于8位!');
                passwordEle.focus();
                return false;}
            if (passwordEleVal != passwordEleVal2){
                window.alert('两次密码不一致！请重新输入!');
                passwordEle2.value='';
                passwordEle2.focus();
                return false;}
            else{
                return true}
            }
        //将用户名和密码及确认密码中的特殊符号换位对应的HTML实体，以防止SQL注入产生
        //SQL注入问题必须重视
        function entities(str){
            str = str.replace(/&/g,'&amp;');
            str = str.replace(/'/g,'&#39;');
            str = str.replace(/"/g,'&quot;');
            str = str.replace(/>/g,'&gt;');
            str = str.replace(/</g,'&lt;');
            str = str.replace(/ /g,'&nbsp;');
            return str;
            }