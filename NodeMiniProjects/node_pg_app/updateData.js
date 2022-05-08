const {pool} = require('./db');

async function updateRow(){
    const [oldData,NewData,id] = process.argv.slice(3);
    try{
        const del = await pool.query(
            'DELETE table1 SET $1 = $2 WHERE id = $3'[oldData,NewData,id]
        );
        console.log("Row Deleted");
    } catch(error){
        console.log(error);
    }
}

updateRow();