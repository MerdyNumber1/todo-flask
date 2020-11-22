let addTaskForm = document.querySelector('.tasks__submit')

if(addTaskForm.length) {
    addTaskForm.onsubmit = async function(e) {
        e.preventDefault()
        fetch('/tasks', {
            method: 'POST',
            body: new FormData(this)
        })
            .then(res => {
                console.log(this.title)
            })
    }
}