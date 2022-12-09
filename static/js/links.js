function get_length(input, small_id){
    let value = input.value;
    document.getElementById(small_id).innerHTML = value.length
}

function check_regex(input, variant){
    const reg = variant
    if (variant){
        const regex = /^([A-Za-z0-9_]{1,}\/{0,1})*$/
    }
    else
    {
        const regex = /^((?:https?\:)?(?:\/{2})?)?((?:[\w\d_]{1,64})\.(?:[\w\d_\.]{2,64}))(\:\d{2,6})?((?:\/|\?|#|&){1}(?:[\w\d\S]+)?)?$/
    }
    if(regex.test(input.value))
    {
        document.getElementById('post-btn').classList.remove('disabled');
        document.getElementById('url-error').classList.add('hidden');
    }
    else
    {
        document.getElementById('url-error').classList.remove('hidden');
        document.getElementById('post-btn').classList.add('disabled');
    }
}