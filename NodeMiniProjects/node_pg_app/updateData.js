const {pool} = require('./db');

async function updateNameRow(NewData,id){
    try{
        const update = await pool.query(
            `UPDATE table1 SET name = '${NewData}' WHERE id = ${id} ;`
        );
        console.log("Row Updated");
    } catch(error){
        console.log(error);
    }
}

updateNameRow("Mikasa",4);