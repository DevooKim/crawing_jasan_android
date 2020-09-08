package com.example.qr

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Toast
import com.google.firebase.database.*
import com.google.zxing.integration.android.IntentIntegrator
import com.google.zxing.integration.android.IntentResult
import org.json.JSONException
import org.json.JSONObject
import java.io.File
import java.io.FileWriter
import java.lang.Exception

class MainActivity : AppCompatActivity() {

    private val intentIntegrator: IntentIntegrator = IntentIntegrator(this)

    val mDatabase: DatabaseReference = FirebaseDatabase.getInstance().reference


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        intentIntegrator.initiateScan()
    }


    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        val result: IntentResult = IntentIntegrator.parseActivityResult(requestCode, resultCode, data)
        if(result != null){
            if(result.contents == null){
                Toast.makeText(this, "Cancelled", Toast.LENGTH_SHORT).show()
            } else {
                Toast.makeText(this, "Scanned: "+result.contents, Toast.LENGTH_SHORT).show()
                var url = result.contents
                url = url.substring(url.length-15, url.length)
                mDatabase.child("PC").child(url).setValue(result.contents)

                intentIntegrator.initiateScan()

            }
        } else {
            super.onActivityResult(requestCode, resultCode, data)
        }
    }


}
