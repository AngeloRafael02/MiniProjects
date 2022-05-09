const {pool} = require('./db');

async function deleteRow(id){
    try{
        const del = await pool.query(
            "DELETE FROM table1 WHERE id = " + id
        );
        console.log("Row Deleted");
    } catch(error){
        console.log(error);
    }
}

deleteRow(3);