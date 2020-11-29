let taskForm = document.querySelector('.tasks__form')

if(taskForm) {
    taskForm.onsubmit = async function(e) {
        e.preventDefault()
        fetch('', {
            method: 'POST',
            body: new FormData(this)
        })
            .then(res => res.json())
            .then(res => {
                console.log(res)
            })
    }
}