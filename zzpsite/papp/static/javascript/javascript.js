
function change_visibility(object)
{
    var d = document.getElementById(object)
    if (d.style.visibility == 'hidden') {
    d.style.visibility = 'visible'
    }
    else {
    d.style.visibility = 'hidden'
    }

}
