// webpack.config.js

module.exports = {
    module: {
      rules: [
        {
          test: /\.s(c|a)ss$/,
          use: [
            'vue-style-loader',
            'css-loader',
            {
              loader: 'sass-loader',
              // Requires sass-loader@^7.0.0
              options: {
                implementation: require('sass'),
                indentedSyntax: true // optional
              },
              // Requires >= sass-loader@^8.0.0
              options: {
                implementation: require('sass'),
                sassOptions: {
                  indentedSyntax: true // optional
                },
              },
            },
          ],
        },
<<<<<<< HEAD
<<<<<<< HEAD
        
=======
=======
>>>>>>> 0ad56b737a8ad05747ee7b606914fb7b58d5022e
        {
          test: /\.(csv|xlsx|xls)$/,
          loader: 'file-loader',
          options: {
              name: `files/[name].[ext]`
          }
      }
<<<<<<< HEAD
>>>>>>> develop
=======
>>>>>>> 0ad56b737a8ad05747ee7b606914fb7b58d5022e
      ],
    }
  }