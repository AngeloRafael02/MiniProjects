import { Component, OnInit } from '@angular/core';
import { ActivatedRoute,Router } from '@angular/router';
import { weaponInterface } from '../interfaces';
import { MainService } from '../main.service';

@Component({
  selector: 'app-weapon-details',
  template:`
  <button (click)="prev()">PREV</button> <button (click)="back()">BACK</button> <button (click)="next()">NEXT</button>
    <p> Name: {{ weapons[weaponNumber].name }}
      {{ weapons[weaponNumber].domain}}
    </p>`,
  styles: [``]
})
export class WeaponDetailsComponent implements OnInit {

  public weapons:weaponInterface[] = [];
  public weaponNumber:number = 0;

  constructor(
    private _mainService:MainService,
    private route:ActivatedRoute,
    private router:Router
  ) { }

  ngOnInit(): void {
    this.weaponNumber = this.route.snapshot.params['id']

    this._mainService.getWeaponView()
    .subscribe(data => this.weapons = data);

    this.route.paramMap.subscribe((params:any)=>{
      let id = parseInt(params.get('id'));
      this.weaponNumber = id;
    });
  }

  prev():void{
    let prevId:number = this.weaponNumber - 1;
    if (prevId < 0) { prevId = 0; }
    this.router.navigate(['/Weapons',prevId])
  }
  back():void{
    let backId = this.weaponNumber 
    this.router.navigate(['/Weapons', {id:backId}]);
  }
  next():void{
    let nextId:number = this.weaponNumber + 1;
    this.router.navigate(["/Weapons",nextId])
  }

}
