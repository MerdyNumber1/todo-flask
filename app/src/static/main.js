let taskForm = document.querySelector('.tasks__form')

if(taskForm) { // form for add new task
    taskForm.onsubmit = async function(e) {
        e.preventDefault()
        fetch('', {
            method: 'POST',
            body: new FormData(this)
        })
            .then(res => res.json())
            .then(res => {
                document.querySelector('.tasks__wrapper').classList.remove('d-none')

                const newTask = document.createElement('li')
                newTask.classList.add('list-group-item')

                const newTaskWrapper = document.createElement('div')
                newTaskWrapper.classList.add('w-100', 'd-flex', 'justify-content-between', 'align-items-center')
                newTaskWrapper.innerText = res.task.title

                const newTaskCheckbox = document.createElement('input')
                newTaskCheckbox.type = 'checkbox'
                res.task.done && (newTaskCheckbox.checked = true)

                newTaskWrapper.appendChild(newTaskCheckbox)
                newTask.appendChild(newTaskWrapper)

                document.querySelector('.tasks__content').appendChild(newTask)
            })
    }
}

let tasks = document.querySelector('.tasks__content')

if(tasks) {
    tasks.onclick = function({target}) {
        if(target.tagName === 'input') {
            fetch('')
        }
    }
}