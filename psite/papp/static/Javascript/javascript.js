
function change_visibility(object)
{
    var d = document.getElementById(object)

    if (d.style.visibility == 'hidden') {
    d.style.visibility = 'visible';
    d.style.height = '300px';
    d.style.width = '300px';
    }
    else {
    d.style.visibility = 'hidden';
    }

}
