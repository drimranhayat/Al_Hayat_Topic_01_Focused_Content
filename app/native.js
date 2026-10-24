import { Capacitor } from '@capacitor/core';
import { App } from '@capacitor/app';
import { Filesystem, Directory, Encoding } from '@capacitor/filesystem';
import { Share } from '@capacitor/share';
if (Capacitor.isNativePlatform()) {
 document.documentElement.classList.add('native-app');
 App.addListener('backButton', ({canGoBack}) => {
  const dialog=document.querySelector('dialog[open]');
  if(dialog){dialog.close();return;}
  if(canGoBack){history.back();return;}
  if(!document.getElementById('exit-app')){
   const d=document.createElement('dialog');d.id='exit-app';
   const text=document.createElement('p');text.textContent='Close Al-Hayat Hadith?';
   const cancel=document.createElement('button');cancel.textContent='Keep reading';cancel.onclick=()=>d.close();
   const exit=document.createElement('button');exit.textContent='Close app';exit.onclick=()=>App.exitApp();
   d.append(text,cancel,exit);document.body.append(d);
  }document.getElementById('exit-app').showModal();
 });
 const backup=document.getElementById('export-notes');
 if(backup)backup.onclick=async()=>{
  const get=(key,fallback)=>{try{return JSON.parse(localStorage.getItem(key))??fallback}catch{return fallback}};
  const prefix='alhayat-topic001-v1';
  const data={format:prefix,exported:new Date().toISOString(),saved:get(prefix+'-saved',[]),read:get(prefix+'-read',[]),notes:get(prefix+'-notes',{}),prefs:get(prefix+'-prefs',{}),quiz:get('alhayat-topic001-v4-coverage-quiz',{})};
  try{
   const file=await Filesystem.writeFile({path:'al-hayat-study-backup.json',data:JSON.stringify(data,null,2),directory:Directory.Cache,encoding:Encoding.UTF8});
   await Share.share({title:'Study backup',files:[file.uri]});
  }catch{const toast=document.getElementById('toast');if(toast){toast.textContent='Backup was not saved. Please try again.';toast.hidden=false}}
 };
 const print=document.getElementById('print');if(print)print.hidden=true;
 const button=document.getElementById('native-share');
 if(button)button.onclick=async()=>{
  const data=window.HADITH_DATA?.find(d=>d.id===document.querySelector('article[data-id]')?.dataset.id);
  if(!data)return;
  try{await Share.share({title:data.title,text:data.ar+'\n\n'+data.en+'\n\n'+data.ref+'\nEnglish translation: HadeethEnc.com\n'+data.source,dialogTitle:'Share hadith with references'});}catch{}
 };
}
