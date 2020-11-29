let taskForm = document.querySelector('.tasks__form')

if (taskForm) { // form for add new task
    taskForm.onsubmit = async function (e) {
        e.preventDefault()
        const data = new FormData(this)

        const [input, button] = document.querySelectorAll('.tasks__add-input, .tasks__submit')
        input.value = ''
        button.disabled = true

        fetch('', {
            method: 'POST',
            body: data
        })
            .then(res => res.json())
            .then(res => {
                document.querySelector('.tasks__wrapper').classList.remove('d-none')

                const newTask = document.createElement('li')
                newTask.classList.add('list-group-item', 'tasks__task')

                newTask.innerHTML = `
                    <div class="w-100 d-flex justify-content-between align-items-center">
                        <div class="d-flex align-items-center">
                            <input style="width: 15px; height: 15px;"
                                   class="tasks__done mr-2 pointer"
                                   data-id="${res.task.id}"
                                   type="checkbox"
                                   ${res.task.done && 'checked'}>
                            <p class="tasks__title m-0">${res.task.title}</p>
                            <input class="tasks__title-input d-none" value="${res.task.title}" type="text">
                        </div>
    
                        <div class="d-flex align-items-center">
                            <img class="tasks__edit mr-2 pointer"
                                 src="/static/node_modules/bootstrap-icons/icons/pencil-square.svg"
                                 alt="">
                            <img data-id="${res.task.id}"
                                 class="tasks__save-edit mr-2 pointer d-none"
                                 src="/static/node_modules/bootstrap-icons/icons/check.svg"
                                 alt="">
                            <img data-id="${res.task.id}"
                                 class="tasks__remove pointer"
                                 src="/static/node_modules/bootstrap-icons/icons/trash.svg"
                                 alt="">
                        </div>
                    </div>
                `

                document.querySelector('.tasks__content').appendChild(newTask)

                button.disabled = false
            })
    }
}

let tasks = document.querySelector('.tasks__content')

if (tasks) {
    tasks.onclick = function ({target}) {
        if (target.className.includes('tasks__done') || target.className.includes('tasks__save-edit')) {

            if (target.className.includes('tasks__save-edit')) toggleEditTask(target.closest('.tasks__task'))
            else target.disabled = true

            const task = target.closest('.tasks__task')
            setTimeout(() => {
                fetch(target.dataset.id, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        title: task.querySelector('.tasks__title').textContent,
                        done: task.querySelector('.tasks__done').checked
                    })
                })
                    .then(res => res.json())
                    .then(() => {
                        target.disabled = false
                    })
            }, 200)
        } else if (target.className.includes('tasks__remove')) {
            fetch(target.dataset.id, {
                method: 'DELETE',
            })
                .then(() => {
                    target.closest('.tasks__task').remove()
                })
        } else if (target.className.includes('tasks__edit')) {
            toggleEditTask(target.closest('.tasks__task'))
        }
    }
}

function toggleEditTask(taskEl) {
    taskEl.querySelector('.tasks__title').innerText = taskEl.querySelector('.tasks__title-input').value
    taskEl.querySelector('.tasks__title').classList.toggle('d-none')
    taskEl.querySelector('.tasks__title-input').classList.toggle('d-none')
    taskEl.querySelector('.tasks__edit').classList.toggle('d-none')
    taskEl.querySelector('.tasks__save-edit').classList.toggle('d-none')
}