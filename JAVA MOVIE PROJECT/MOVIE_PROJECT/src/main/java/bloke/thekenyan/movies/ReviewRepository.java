package bloke.thekenyan.movies;

import org.bson.types.ObjectId;
import org.springframework.stereotype.Repository;
import org.springframework.data.mongodb.repository.MongoRepository;

@Repository
public interface ReviewRepository extends MongoRepository<Review, ObjectId>{
}
