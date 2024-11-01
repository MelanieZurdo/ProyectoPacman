import { Injectable, inject } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, RouterStateSnapshot, UrlTree } from '@angular/router';
import { FirebaseService } from '../services/firebase.service';
import { Observable } from 'rxjs';
import { UtilsService } from '../services/utils.service';

@Injectable({
  providedIn: 'root'
})

export class AuthGuard implements CanActivate {

  firebaseSvc = inject(FirebaseService);
  utilSvc = inject(UtilsService);
/**
 * @function canActivate
 * @description Funcion que se encarga de verificar si no existe un usuario logueado, q el mismo no pueda 
 * navegar a la secciones internas de la aplicacion y redirige a la seccion de loguin.
 */
  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {

    let user = localStorage.getItem('user');

    return new Promise((resolve) => {

      this.firebaseSvc.getAuth().onAuthStateChanged((auth) => {

        if (auth) {
          if (user) resolve(true);
        } else {
          this.utilSvc.routerLink('/auth');
          resolve(false);
        }
      });
    });
  }
}
