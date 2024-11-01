import { Injectable, inject } from '@angular/core';
import { AngularFireAuth } from '@angular/fire/compat/auth';
import {
  getAuth,
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword,
  updateProfile,
  sendPasswordResetEmail,
} from 'firebase/auth';
import { User } from '.././models/user.model';
import { AngularFirestore } from '@angular/fire/compat/firestore';
import { getFirestore, setDoc, doc, getDoc, addDoc, collection , updateDoc} from '@angular/fire/firestore';
import { UtilsService } from './utils.service';
import { AngularFireStorage } from '@angular/fire/compat/storage';
import { getStorage, uploadString, ref, getDownloadURL} from 'firebase/storage'


@Injectable({
  providedIn: 'root',
})
export class FirebaseService {

  auth = inject(AngularFireAuth);
  firestore = inject(AngularFirestore);
  storage = inject(AngularFireStorage);
  utilsSvc = inject(UtilsService);
  
  /** 
  * @function getAuth
  * @description Función para inciar sesion en firebase
  */
  getAuth(){
    return getAuth();
  }

  /**
   * @function signIn
   * @description Función para iniciar sesion y autenticar datos del usuario con firebase
   */
  signIn(user: User) {
    return signInWithEmailAndPassword(getAuth(), user.email, user.password);
  }

  /**
   * @function signUp
   * @description Función para crear usuario, almacenar mail y contraseña del mismo en firebase
   */
  signUp(user: User) {
    return createUserWithEmailAndPassword(getAuth(), user.email, user.password);
  }

  /**
   * @function signOut
   * @description Función para cerrar sesion y eliminar datos del usuario del localStorage
   */
  signOut() {
    getAuth().signOut();
    localStorage.removeItem('user');
    this.utilsSvc.routerLink('/auth');
  }

  /**
   * @function updateUser
   * @description Función para actualizar el nombre del usuario de la bbdd con el nombre recibido por parametro. 
   */
  updateUser(displayName: string) {
    return updateProfile(getAuth().currentUser, { displayName });
  }

  /**
   * @function sendRecoveryEmail
   * @description Función para enviar email y resetear contraseña del usuario
   */
  sendRecoveryEmail(email: string){
    return sendPasswordResetEmail(getAuth(), email)
  }
  
  /**
   * @function setDocument
   * @description Función para almacenar un nuevo documento en la bbdd de firebase, el mismo puede tener 
   * (mail, nombre, image, uuid)
   */
  setDocument(path: string, data: any) {
    return setDoc(doc(getFirestore(), path), data);
  }

 /**
  * @function getDocument
  * @description Funcion para obtener documento almacenado de la bbdd de firebase por medio del path 
  * recibido el cual tiene el uuid del usuario logueado
  */
  async getDocument(path: string) {
    return (await getDoc(doc(getFirestore(), path))).data();
  }
 
 /**
  * @function uploadImage
  * @param data_url 
  * @description Función para guardar imagen de perfil del usuario en el documento creado en la bbdd de 
  * firebase, bajo su uuid
  */
  async uploadImage(path: string, data_url: any) {
    return uploadString(ref(getStorage(), path), data_url, 'data_url').then(() => {
      return getDownloadURL(ref(getStorage(), path))
    })
  }

 /**
  * @function getFilePath
  * @description Función para obtener imagen de la bbdd de firebase, bajo el uuid del usuario logueado
  */
  async getFilePath(url: string): Promise<string> {
    const storage = getStorage();
    const storageRef = ref(storage, url);
    return await getDownloadURL(storageRef);
  }

 /**
  * @function updateDocument
  * @description Función para actualizar imagen obtenida de la bbdd del usuario al loguearse, por la imagen
  *  modificada por el usuario. 
  */
  updateDocument(path: string, data: any) {
    return updateDoc(doc(getFirestore(), path), data)
  }
}