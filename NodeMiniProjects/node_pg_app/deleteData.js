const {pool} = require('./db');

async function deleteRow(){
    const [id] = process.argv.slice(1);
    try{
        const del = await pool.query(
            'DELETE FROM table1 WHERE id = $1;'[id]
        );
        console.log("Row Deleted");
    } catch(error){
        console.log(error);
    }
}

deleteRow();