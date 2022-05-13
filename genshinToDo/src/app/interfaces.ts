export interface characterInterface {
    id:Number,
    star:Number,
    name:String,
    weaponType:String,
    element:String,
    region:String,  
    domain:String,
    material:String,
    availability:String[]
}

export interface weaponInterface{
    id:Number,
    star:Number,
    name:String,
    secondaryStat:String,
    weaponType:String,
    domain:String,
    material:String,
    availability:String[]
}