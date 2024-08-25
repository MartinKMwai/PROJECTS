package bloke.thekenyan.movies;

import lombok.Data;
import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.DocumentReference;
import org.bson.types.ObjectId;
import java.util.List;

@Document(collection = "movies")

@Data //generates getters and setters rather than creating them myself
@AllArgsConstructor //generates constructors that takes all these private fields as arguments
@NoArgsConstructor //generates a constructor with no arguments
public class Movie {
    @Id //showing that ObjectId will be used as the unique identifier in the database
    private ObjectId id;
    private String imdbId;
    private String movieTitle;
    private String releaseDate;
    private String trailerLink;
    private String poster;
    private List<String> genres;
    private List<String> backdrops;

    @DocumentReference //one-to-many relationship : one movie, many reviews
    private List<Review> reviewIds;
}
