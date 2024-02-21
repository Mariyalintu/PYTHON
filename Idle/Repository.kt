
    package com.example.autonavpro

    object Repository {
        // Fragment1
        var Fragment1: String = "Mariya"
        fun setFragment1Text(value: String) {
            Fragment1 = value
            // Log.d("Johnsoft", "Fragment1 text set: $value")
        }
        fun getFragment1Text(): String {
            val text = Fragment1
            // Log.d("Johnsoft", "Fragment1 text retrieved: $text")
            return text
        }

        // Fragment 2
        var Fragment2: String = "Lintuu"
        fun setFragment2Text(value: String) {
            Fragment2 = value
            // Log.d("Johnsoft", "Fragment2 text set: $value")
        }
        fun getFragment2Text(): String {
            val text = Fragment2
            // Log.d("Johnsoft", "Fragment2 text retrieved: $text")
            return text
        }
    }
    