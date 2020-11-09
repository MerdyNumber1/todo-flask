db.createUser({
    user: 'merdy',
    pwd: 'merdy',
    roles: [{
        role: 'readWrite',
        db: 'todo'
    }]
})
